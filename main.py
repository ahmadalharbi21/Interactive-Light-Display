import asyncio
import time
from bleak import BleakClient
import threading
from dxcam_capture import run_dxcam_capture, color_queue
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="RGB Light Control")
    parser.add_argument("--fps", type=int, default=144, help="Target FPS for camera capture")
    parser.add_argument("--delay", type=float, default=0.04, help="Delay time between requests (in seconds)")
    parser.add_argument("--resize", nargs=2, type=int, default=[300, 250], help="Resize shape for image processing")
    #parser.add_argument("--header", type=str, default="~\\x07\\x05\\x03", help="Header bytes for color request")
    #parser.add_argument("--rgb-position", type=int, default=4, help="Position to insert RGB values in color bytes")
    #parser.add_argument("--tail", type=str, default="~\\x10\\xefNR1713\\x01", help="Tail bytes for color request")
    parser.add_argument("--device-address", type=str, default="BE:16:F7:00:03:B9", help="Device address")
    parser.add_argument("--characteristic-uuid", type=str, default="0000fff3-0000-1000-8000-00805f9b34fb", help="Characteristic UUID")
    return parser.parse_args()

async def send_color(client, r, g, b, characteristic_uuid):
    color_bytes = bytearray(b"~\x07\x05\x03")
    color_bytes += bytes([r, g, b])
    color_bytes += bytearray(b"\x10\xefNR1713\x01")
    await client.write_gatt_char(characteristic_uuid, color_bytes)

async def run_bleak_client(args):
    try:
        async with BleakClient(args.device_address) as client:
            print(f"Connected: {client.is_connected}")
            initial_value = await client.read_gatt_char(args.characteristic_uuid)
            print(f"Initial value of characteristic: {initial_value}")
            while True:
                if color_queue:
                    r, g, b = color_queue.popleft()
                    await send_color(client, r, g, b, args.characteristic_uuid)
                else:
                    await asyncio.sleep(args.delay)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    args = parse_arguments()
    bleak_thread = threading.Thread(target=asyncio.run, args=(run_bleak_client(args),))
    dxcam_thread = threading.Thread(target=run_dxcam_capture, args=(args,))
    bleak_thread.start()
    dxcam_thread.start()
    bleak_thread.join()
    dxcam_thread.join()
    print("All operations completed.")

if __name__ == "__main__":
    main()