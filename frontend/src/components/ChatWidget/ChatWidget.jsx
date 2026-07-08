import { useState } from "react";
import "./ChatWidget.css";
import ReactMarkdown from "react-markdown";

function ChatWidget() {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content:
        "Hi, I’m PVW’s AI Concierge. I can help you find watches, compare models, check availability, or make an enquiry.",
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      role: "user",
      content: input,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: userMessage.content,
        }),
      });

      const data = await res.json();

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: data.response || "Sorry, I couldn't get a response.",
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Sorry, the AI assistant is currently unavailable. Please try again later.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      {isOpen && (
        <div className="chat-window">
          <div className="chat-header">
            <div>
              <strong>PVW AI Concierge</strong>
              <span>Vintage Watch Assistant</span>
            </div>
            <button onClick={() => setIsOpen(false)}>×</button>
          </div>

          <div className="chat-messages">
            {messages.map((msg, index) => (
              <div key={index} className={`chat-message ${msg.role}`}>
                <ReactMarkdown>{msg.content}</ReactMarkdown>
              </div>
            ))}

            {loading && (
              <div className="chat-message assistant">Thinking...</div>
            )}
          </div>

          <div className="chat-input-area">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter") sendMessage();
              }}
              placeholder="Ask about watches..."
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </div>
      )}

      <button className="ai-chat-button" onClick={() => setIsOpen(true)}>
        AI
      </button>
    </>
  );
}

export default ChatWidget;
