document.addEventListener("DOMContentLoaded", () => {
    const chatWindow = document.getElementById("chat-window");
    const userInput = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const loadingIndicator = document.getElementById("loading");

    const API_URL = "http://127.0.0.1:8000/api/ask-agent";

    const addMessage = (text, sender) => {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", `${sender}-message`);
        messageElement.innerText = text;
        chatWindow.appendChild(messageElement);
        chatWindow.scrollTop = chatWindow.scrollHeight; // Rola para a última mensagem
    };

    const handleSend = async () => {
        const query = userInput.value.trim();
        if (!query) return;

        addMessage(query, "user");
        userInput.value = "";
        loadingIndicator.style.display = "block";

        try {
            const response = await fetch(API_URL, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ query: query }),
            });

            if (!response.ok) {
                throw new Error("A resposta da rede não foi 'ok'.");
            }

            const data = await response.json();
            addMessage(data.answer, "bot");

        } catch (error) {
            console.error("Erro ao buscar resposta:", error);
            addMessage("Desculpe, não consegui me conectar ao meu cérebro. Tente novamente mais tarde.", "bot");
        } finally {
            loadingIndicator.style.display = "none";
        }
    };

    sendBtn.addEventListener("click", handleSend);
    userInput.addEventListener("keyup", (event) => {
        if (event.key === "Enter") {
            handleSend();
        }
    });

    // Mensagem inicial
    addMessage("Olá! Como posso te ajudar a planejar sua viagem hoje?", "bot");
});