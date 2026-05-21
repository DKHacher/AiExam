import { useState } from "react"

function App() {
    const [result, setResult] = useState(
        "AI responses will appear here..."
    )
    const [message, setMessage] = useState("")
    const [loading, setLoading] = useState(false)
    
async function sendMessage() {

        if (!message.trim()) return

        setLoading(true)

        try {

            const response = await fetch(
                "http://localhost:8000/chat",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        message: message,
                        model: "qwen2.5:7b"
                    })
                }
            )

            const data = await response.json()

            setResult(data.response)

        } catch (error) {

            setResult("Error connecting to backend.")

        }

        setLoading(false)
    }

     return (
        <div className="App">

            <header className="Header">
                <h1>AI TCG Prediction Tool</h1>
            </header>

            <main className="ResultBox">
                <div className="Result">

                    {loading
                        ? "Loading..."
                        : result}

                </div>
            </main>

            <footer className="Functions">

                <input
                    type="text"
                    placeholder="Ask about a card..."
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                />

                <button onClick={sendMessage}>
                    Send
                </button>

            </footer>

        </div>
    )
}


export default App