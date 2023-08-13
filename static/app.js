let copyToClipboard = (e) => {
    let currentTarget = e.currentTarget;
    navigator.permissions.query({name: "clipboard-write"}).then(result => {
        if (result.state === "granted" || result.state === "prompt") {
            // Clipboard access is granted. Use it to write to the clipboard
            const text = document.getElementById(`${currentTarget.id}-text`).innerText;
            try {
                navigator.clipboard.writeText(text);
                console.log('Text copied to clipboard');
            } catch (err) {
                console.log('Failed to copy text: ', err);
            }
        } else {
            console.log('Clipboard access denied');
        }
    }).catch(err => {
        console.log('Clipboard access denied: ', err);
    });
}