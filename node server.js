const fs = require("fs");
const login = require("facebook-chat-api");
const http = require("http");

// Render Port Binding Error से बचने के लिए सर्वर
const PORT = process.env.PORT || 3000;
http.createServer((req, res) => {
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("Facebook Convo Server is Running!");
}).listen(PORT);

const TARGET_THREAD_ID = "YOUR_TARGET_CHAT_ID"; // यहाँ टारगेट आईडी डालें
const TIME_DELAY = 5000; 

let tokenData = JSON.parse(fs.readFileSync("appstate.json", "utf8"));

login({ appState: tokenData }, (err, api) => {
    if (err) return console.error("टोकन एक्सपायर या अमान्य है:", err);

    console.log("फेसबुक आईडी सफलतापूर्वक कनेक्ट हो गई!");

    let messages = fs.readFileSync("np.txt", "utf-8").split(/\r?\n/).filter(line => line.trim() !== "");
    let messageIndex = 0;

    function sendConvo() {
        if (messageIndex >= messages.length) messageIndex = 0; 

        const msgToSend = messages[messageIndex];
        api.sendMessage(msgToSend, TARGET_THREAD_ID, (sendErr) => {
            if (!sendErr) {
                console.log(`भेजा गया: ${msgToSend}`);
                messageIndex++;
            } else {
                console.error("भेजने में एरर:", sendErr);
            }
            setTimeout(sendConvo, TIME_DELAY);
        });
    }
    sendConvo();
});
