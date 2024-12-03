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
      <pre><code>git clone &lt;repo-url&gt;</code></pre>
    </li>
    <li>
      Install dependencies:
      <pre><code>pip install bleak dxcam</code></pre>
    </li>
    <li>
      Run the script:
      <pre><code>python interactive_led.py</code></pre>
    </li>
  </ol>
  <hr />
  <h3>Example in Action</h3>
  <p>
    <img src="Example.gif" alt="Interactive Lighting Demo" />
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
  <p><strong>Note:</strong> You need to find your specific <code>DEVICE_ADDRESS</code> and <code>CHARACTERISTIC_UUID</code> for the LED light. A custom BLE exploration tool has been built to help with this.</p>
  <p>
    <a href="&lt;insert-link-here&gt;" target="_blank">BLE Device Explorer Tool Repository</a>
  </p>
  <hr />
  <h3>Acknowledgements</h3>
  <ul>
    <li>
      <strong>dxcam</strong>: Used for low-latency screen capturing. Learn more
      <a href="https://github.com/SerpentAI/dxcam" target="_blank">here</a>.
    </li>
    <li>
      <strong>Bleak</strong>: Lightweight and efficient library for Bluetooth communication. Learn more
      <a href="https://github.com/hbldh/bleak" target="_blank">here</a>.
    </li>
  </ul>
  <hr />
  <p>Enhance your entertainment setup with interactive lighting today! 🚀</p>
</div>
