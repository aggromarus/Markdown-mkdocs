document.addEventListener("DOMContentLoaded", function () {
    function encode64(data) {
        return unescape(encodeURIComponent(data))
            .split('')
            .map(char => char.charCodeAt(0))
            .map(byte => String.fromCharCode((byte >> 2) & 63 | 32))
            .join('');
    }

    document.querySelectorAll("code.language-plantuml").forEach(block => {
        const encoded = encode64(block.innerText);
        const img = document.createElement("img");
        img.src = "http://www.plantuml.com/plantuml/svg/" + encoded;
        block.replaceWith(img);
    });
});