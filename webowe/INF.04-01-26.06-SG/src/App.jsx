import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css'

function App() {
  const [address, setAddress] = useState('')
  const [login, setLogin] = useState('')
  const [password, setPassword] = useState('')
  const [generatePassword, setGeneratePassword] = useState(true)

  const [summary, setSummary] = useState({
    address: '',
    login: '',
    password: '',
    generated: true,
  })

  const handleSubmit = (e) => {
    e.preventDefault()
    setSummary({
      address: address,
      login: login,
      password: password,
      generated: generatePassword,
    })
  }

  return (
    <div className="container">
      <div>
        <h1>Menedżer haseł - wykonał 00000000000</h1>
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="address" className="form-label">Adres WWW:</label>
            <input
              type="text"
              className="form-control"
              id="address"
              placeholder="Adres strony WWW"
              value={address}
              onChange={(e) => setAddress(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <label htmlFor="login" className="form-label">Login:</label>
            <input
              type="text"
              className="form-control"
              id="login"
              placeholder="Twój login"
              value={login}
              onChange={(e) => setLogin(e.target.value)}
            />
          </div>
          <div className="mb-3">
            <input
              type="checkbox"
              className="form-check-input"
              id="generatePassword"
              checked={generatePassword}
              onChange={(e) => setGeneratePassword(e.target.checked)}
            />
            <label htmlFor="generatePassword" className="form-check-label ms-1">Wygeneruj hasło</label>
            <br />
            <label htmlFor="password" className="form-label">Hasło:</label>
            <input
              type="password"
              className="form-control"
              id="password"
              disabled={generatePassword}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button type="submit" className="btn btn-primary">Zapisz</button>
        </form>
      </div>
      <div>
        <p className="p-2 text-primary lead">Adres: {summary.address}</p>
        <p className="p-2">Login: {summary.login}</p>
        <p className="p-2">
          {summary.generated ? 'Hasło automatycznie generowane' : `Hasło: ${summary.password}`}
        </p>
      </div>
    </div>
  )
}

export default App
