body {
    margin: 0;
    background: #0f172a;
    font-family: Arial;
    color: white;
}

.chat-container {
    max-width: 500px;
    margin: auto;
    height: 100vh;
    display: flex;
    flex-direction: column;
    padding: 10px;
}

#chat-box {
    flex: 1;
    overflow-y: auto;
    margin-bottom: 10px;
}

p {
    background: #1e293b;
    padding: 8px;
    border-radius: 8px;
}

.input-area {
    display: flex;
}

input {
    flex: 1;
    padding: 10px;
    border: none;
    outline: none;
}

button {
    padding: 10px;
    background: #38bdf8;
    border: none;
    color: black;
}