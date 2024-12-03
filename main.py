import threading
from bleak import BleakClient
from dxcam_capture import run_dxcam_capture, color_queue

# Fixed configuration values
FPS = 144
DELAY = 0.04
RESIZE_SHAPE = [300, 250]
DEVICE_ADDRESS = "BE:16:F7:00:03:B9"
CHARACTERISTIC_UUID = "0000fff3-0000-1000-8000-00805f9b34fb"

async def send_color(client, r, g, b, characteristic_uuid):
    color_bytes = bytearray(b"~\x07\x05\x03")
    color_bytes += bytes([r, g, b])
    color_bytes += bytearray(b"\x10\xefNR1713\x01")
    await client.write_gatt_char(characteristic_uuid, color_bytes)

async def run_bleak_client():
    try:
        async with BleakClient(DEVICE_ADDRESS) as client:
            print(f"Connected: {client.is_connected}")
            initial_value = await client.read_gatt_char(CHARACTERISTIC_UUID)
            print(f"Initial value of characteristic: {initial_value}")
            while True:
                if color_queue:
                    r, g, b = color_queue.popleft()
                    await send_color(client, r, g, b, CHARACTERISTIC_UUID)
                else:
                    await asyncio.sleep(DELAY)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    bleak_thread = threading.Thread(target=asyncio.run, args=(run_bleak_client(),))
    dxcam_thread = threading.Thread(target=run_dxcam_capture, args=(FPS, DELAY, RESIZE_SHAPE))
    bleak_thread.start()
    dxcam_thread.start()
    bleak_thread.join()
    dxcam_thread.join()
    print("All operations completed.")

if __name__ == "__main__":
    main()
