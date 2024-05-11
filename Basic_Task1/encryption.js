let key;

async function generateKey() {
    if (!key) {
        key = await window.crypto.subtle.generateKey(
            { name: "AES-GCM", length: 256 },
            true,
            ["encrypt", "decrypt"]
        );
    }
    return key;
}

async function encryptText() {
    try {
        const inputText = document.getElementById("inputText").value;
        const encoder = new TextEncoder();
        const encodedText = encoder.encode(inputText);
        const iv = window.crypto.getRandomValues(new Uint8Array(12));
        const key = await generateKey();
        const encryptedData = await window.crypto.subtle.encrypt(
            { name: "AES-GCM", iv: iv },
            key,
            encodedText
        );
        const encryptedArray = new Uint8Array(encryptedData);
        const resultArray = new Uint8Array(iv.length + encryptedArray.length);
        resultArray.set(iv, 0);
        resultArray.set(encryptedArray, iv.length);
        const encryptedText = btoa(String.fromCharCode.apply(null, resultArray));
        document.getElementById("encryptedText").innerText = encryptedText;
    } catch (error) {
        console.error("Encryption error:", error);
    }
}

async function decryptText() {
    try {
        const encryptedText = atob(document.getElementById("encryptedInput").value);
        const encryptedArray = new Uint8Array(encryptedText.match(/[\s\S]/g).map(ch => ch.charCodeAt(0)));
        const iv = encryptedArray.slice(0, 12);
        const ciphertext = encryptedArray.slice(12);
        const key = await generateKey();
        const decryptedData = await window.crypto.subtle.decrypt(
            { name: "AES-GCM", iv: iv },
            key,
            ciphertext
        );
        const decryptedText = new TextDecoder().decode(decryptedData);
        document.getElementById("decryptedText").innerText = decryptedText;
    } catch (error) {
        console.error("Decryption error:", error);
    }
}