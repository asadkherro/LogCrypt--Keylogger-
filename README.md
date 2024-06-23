<h1>📄 LogCrypt: Keylogger Documentation 📄 </h1>
    <h2>Overview:</h2>
    <p>LogCrypt is a secure keylogger designed to capture keystrokes while prioritizing data security through encryption. The keylogger operates in the background, monitoring user input and storing the logged data in an encrypted format. This documentation outlines the architecture and working principles of LogCrypt.</p>
    <h2>Architecture:</h2>
    <p>LogCrypt employs a simple yet robust architecture consisting of the following components:</p>
    <ol>
        <li><strong>Keyboard Listener:</strong> Utilizes the <code>pynput</code> library to capture keystrokes in real-time.</li>
        <li><strong>Encryption Module:</strong> Utilizes the <code>cryptography</code> library to encrypt the captured keystrokes before writing them to the log file.</li>
        <li><strong>Log File:</strong> Stores the encrypted keystrokes in a log file for later retrieval and decryption.</li>
        <li><strong>Key Manager:</strong> Manages the encryption key, ensuring secure storage and retrieval.</li>
    </ol>
    <h2>Methods Employed:</h2>
    <h3>1. Keyboard Listener ⌨️ :</h3>
    <ul>
        <li>Utilizes the <code>pynput</code> library to create a listener for keyboard events.</li>
        <li>Captures keystrokes using the <code>on_press</code> function.</li>
        <li>Differentiates between printable characters and special keys (e.g., space, enter) to log them appropriately.</li>
    </ul>
    <h3>2. Encryption Module 🔐 :</h3>
    <ul>
        <li>Utilizes the <code>cryptography</code> library to implement encryption and decryption functionalities.</li>
        <li>Generates and manages an encryption key using the <code>KeyManager</code> class.</li>
        <li>Encrypts the captured keystrokes before writing them to the log file.</li>
        <li>Decrypts the log file when reading it for retrieval.</li>
    </ul>
    <h3>3. Log File Management 📝 :</h3>
    <ul>
        <li>Logs the encrypted keystrokes to a designated log file (<code>encrypted_log.txt</code>).</li>
        <li>Appends each encrypted keystroke to the log file, ensuring continuous logging.</li>
        <li>Provides a secure storage mechanism for the captured data.</li>
    </ul>
    <h2>Working Principle:</h2>
    <ol>
        <li><strong>Initialization:</strong>
            <ul>
                <li>LogCrypt initializes by generating or retrieving the encryption key using the <code>KeyManager</code> class.</li>
                <li>The encryption key is used to initialize the Fernet cipher for encryption and decryption.</li>
            </ul>
        </li>
        <li><strong>Keystroke Capture:</strong>
            <ul>
                <li>LogCrypt listens for keyboard events using the <code>pynput</code> library.</li>
                <li>When a keystroke is detected, it is encrypted using the Fernet cipher and written to the log file.</li>
            </ul>
        </li>
        <li><strong>Data Encryption:</strong>
            <ul>
                <li>Before writing to the log file, each keystroke is encrypted using the Fernet cipher initialized with the encryption key.</li>
            </ul>
        </li>
        <li><strong>Data Retrieval:</strong>
            <ul>
                <li>To retrieve the logged data, the log file is read and decrypted using the encryption key.</li>
                <li>The decrypted keystrokes are then displayed or processed as needed by the user.</li>
            </ul>
        </li>
    </ol>
<h2>Flow:</h2>
    <pre>
                 +-------------------+
                 |                   |
      Keystrokes |    Keyboard       |
      +---------> |    Listener       |
                 |                   |
                 +--------+----------+
                          |
                          v
                 +--------+----------+
                 |                   |
                 |    LogCrypt        |
                 |    Keylogger       |
                 |                   |
                 +--------+----------+
                          |
                          v
                 +--------+----------+
                 |                   |
                 |    Encryption      |
                 |    Module         |
                 |                   |
                 +--------+----------+
                          |
                          v
                 +--------+----------+
                 |                   |
                 |    Log File        |
                 |                   |
                 +-------------------+
    </pre>
    <h2>Conclusion:</h2>
    <p>LogCrypt provides a secure solution for capturing and logging keystrokes while prioritizing data security through encryption. By employing robust encryption techniques and secure data handling practices, LogCrypt ensures that logged data remains confidential and protected from unauthorized access.</p>
