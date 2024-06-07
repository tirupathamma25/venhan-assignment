let containerEl = document.createElement("div");
containerEl.style.textAlign = "center";
document.body.appendChild(containerEl);

let h1Element = document.createElement("h1");
h1Element.textContent = "JavaScript Basics";
h1Element.style.color = "blue";
containerEl.appendChild(h1Element);

let btnElement = document.createElement("button");
btnElement.textContent = "Alert";
btnElement.style.height = "30px";
btnElement.style.width = "70px";
btnElement.style.color = "white";
btnElement.style.border = "none";
btnElement.style.backgroundColor = "green";

containerEl.appendChild(btnElement);

function showAlert() {
    alert("Hello, this is a JavaScript alert!");
}

containerEl.addEventListener("click", showAlert);