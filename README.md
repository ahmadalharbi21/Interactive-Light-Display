<div class="markdown prose w-full break-words dark:prose-invert dark">
  <h1>Interactive LED Light System Based on Screen Color</h1>
  <h3>Project Description</h3>
  <p>This project brings your entertainment experience to life by synchronizing LED light colors with the dominant colors of your screen. Using <strong>Bleak</strong> for Bluetooth connectivity and <strong>dxcam</strong> for screen capturing, this system minimizes latency to provide a seamless interactive lighting experience. It’s perfect for gaming, movie watching, or creating an immersive workspace.</p>
  <hr />
  <h3>Features</h3>
  <ul>
    <li><strong>Dynamic Lighting</strong>: The LED lights change in real-time to match the colors on your screen.</li>
    <li><strong>Low Latency</strong>: Utilizes <strong>dxcam</strong> for screen capture, significantly reducing delay compared to alternatives like PIL.</li>
    <li><strong>Bluetooth Control</strong>: Connects to LED lights via Bluetooth using <strong>Bleak</strong>, enabling wireless operation.</li>
  </ul>
  <hr />
  <h3>Required Components</h3>
  <ul>
    <li>LED light strip (product link: <a href="https://www.amazon.sa/dp/B0B419KW6R?ref=ppx_yo2ov_dt_b_fed_asin_title" target="_blank">LED Lights on Amazon</a>)</li>
    <li>Bluetooth-enabled device</li>
    <li>A computer running Python</li>
  </ul>
  <hr />
  <h3>Installation and Usage</h3>
  <ol>
    <li>
      Clone this repository:
      <pre><code>git clone https://github.com/ahmadalharbi21/Interactive-Light-Display</code></pre>
    </li>
    <li>
      Install dependencies using the requirements file:
      <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>
      Run the main script:
      <pre><code>python main.py</code></pre>
    </li>
  </ol>
  <hr />
  <h3>Example in Action</h3>
  <p>
    <img src="Content/Example.gif" alt="Interactive Lighting Demo" />
  </p>
  <p><em>(This example demonstrates the functionality of the LED light system in real-time.)</em></p>
  <hr />
  <h3>Variables to Customize</h3>
  <p>You can tweak the following variables in the script to optimize performance for your setup:</p>
  <pre><code>FPS = 144  # Frames per second for screen capture
DELAY = 0.04  # Delay between frame captures (in seconds)
RESIZE_SHAPE = [300, 250]  # Resolution for screen capture processing
DEVICE_ADDRESS = "BE:16:F7:00:03:B9"  # Replace with your LED device's Bluetooth address
CHARACTERISTIC_UUID = "0000fff3-0000-1000-8000-00805f9b34fb"  # Replace with your LED's UUID</code></pre>
  <p><strong>Note:</strong> Every LED light is different in terms of the request structure. Experiment with your LED light to determine where to pass the RGB values. Modify this part of the code:</p>
  <pre><code>color_bytes = bytearray(b"~\x07\x05\x03")
color_bytes += bytes([r, g, b])
color_bytes += bytearray(b"\x10\xefNR1713\x01")</code></pre>
  <p>To identify the correct property, look for a characteristic without a response. Adjust the colors in the app and monitor the corresponding changes in the property value. This will help you figure out where to pass the RGB values.</p>
  <hr />
  <h3>Performance Optimization</h3>
  <p>Adjust the following variables to achieve the best performance in terms of delay and speed:</p>
  <ul>
    <li><strong>FPS</strong>: Higher values increase screen capture speed but may overload the LED device.</li>
    <li><strong>DELAY</strong>: Reduce delay to improve responsiveness.</li>
    <li><strong>RESIZE_SHAPE</strong>: Lower resolution can speed up processing at the cost of accuracy.</li>
  </ul>
  <p>Each LED light has a limit on how many requests it can handle per second. If you exceed the buffer size, you might experience skipped colors or other unexpected behavior. For example, my LED light can handle requests in the range of 7-9 milliseconds, which corresponds to approximately 120 FPS.</p>
  <hr />
  <h3>Additional Tools</h3>
  <p>To identify your specific <code>DEVICE_ADDRESS</code> and <code>CHARACTERISTIC_UUID</code>, you can use the BLE Device Scanner tool available here:</p>
  <p><a href="https://github.com/ahmadalharbi21/BLE_DEVICE_SCANNER" target="_blank">BLE Device Scanner Repository</a></p>
  <hr />
  <h3>Acknowledgements</h3>
  <ul>
    <li>
      <strong>dxcam</strong>: Used for low-latency screen capturing. Learn more
      <a href="https://github.com/ra1nty/DXcam" target="_blank">here</a>.
    </li>
    <li>
      <strong>Bleak</strong>: Lightweight and efficient library for Bluetooth communication. Learn more
      <a href="https://github.com/hbldh/bleak" target="_blank">here</a>.
    </li>
  </ul>
</div>
