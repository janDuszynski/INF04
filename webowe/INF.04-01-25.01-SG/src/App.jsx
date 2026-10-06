import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css'
import './App.css'

const zdjecia = [
  {id: 0, alt: "Mak", filename: "obraz1.jpg", category: 1, downloads: 35},
  {id: 1, alt: "Bukiet", filename: "obraz2.jpg", category: 1, downloads: 43},
  {id: 2, alt: "Dalmatyńczyk", filename: "obraz3.jpg", category: 2, downloads: 2},
  {id: 3, alt: "Świnka morska", filename: "obraz4.jpg", category: 2, downloads: 53},
  {id: 4, alt: "Rotwailer", filename: "obraz5.jpg", category: 2, downloads: 43},
  {id: 5, alt: "Audi", filename: "obraz6.jpg", category: 3, downloads: 11},
  {id: 6, alt: "kotki", filename: "obraz7.jpg", category: 2, downloads: 22},
  {id: 7, alt: "Róża", filename: "obraz8.jpg", category: 1, downloads: 33},
  {id: 8, alt: "Świnka morska", filename: "obraz9.jpg", category: 2, downloads: 123},
  {id: 9, alt: "Foksterier", filename: "obraz10.jpg", category: 2, downloads: 22},
  {id: 10, alt: "Szczeniak", filename: "obraz11.jpg", category: 2, downloads: 12},
  {id: 11, alt: "Garbus", filename: "obraz12.jpg", category: 3, downloads: 321}
]

const kategorie = [
  {numer: 1, nazwa: "Kwiaty"},
  {numer: 2, nazwa: "Zwierzęta"},
  {numer: 3, nazwa: "Samochody"}
]

function App() {
  const [galeria, setGaleria] = useState(zdjecia)
  const [wlaczone, setWlaczone] = useState([1, 2, 3])

  function zmienKategorie(numer) {
    if (wlaczone.includes(numer)) {
      setWlaczone(wlaczone.filter((k) => k !== numer))
    } else {
      setWlaczone([...wlaczone, numer])
    }
  }

  function pobierz(id) {
    setGaleria(
      galeria.map((zdjecie) =>
        zdjecie.id === id
          ? { ...zdjecie, downloads: zdjecie.downloads + 1 }
          : zdjecie
      )
    )
  }

  return (
    <>
      <h1>Kategorie zdjęć</h1>
      <div>
        {kategorie.map((kategoria) => (
          <div className="form-check form-switch form-check-inline" key={kategoria.numer}>
            <input
              className="form-check-input"
              type="checkbox"
              id={"kategoria" + kategoria.numer}
              checked={wlaczone.includes(kategoria.numer)}
              onChange={() => zmienKategorie(kategoria.numer)}
            />
            <label className="form-check-label" htmlFor={"kategoria" + kategoria.numer}>
              {kategoria.nazwa}
            </label>
          </div>
        ))}
      </div>
      <div className="galeria">
        {galeria.map((zdjecie) =>
          wlaczone.includes(zdjecie.category) ? (
            <div className="blok" key={zdjecie.id}>
              <img src={"/assets/" + zdjecie.filename} alt={zdjecie.alt} />
              <h4>Pobrań: {zdjecie.downloads}</h4>
              <button className="btn btn-success" onClick={() => pobierz(zdjecie.id)}>
                Pobierz
              </button>
            </div>
          ) : null
        )}
      </div>
    </>
  )
}

export default App
