import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.css';

const initialData = [
    { id: 0, alt: "Mak", filename: "obraz1.jpg", category: 1, downloads: 35 },
    { id: 1, alt: "Bukiet", filename: "obraz2.jpg", category: 1, downloads: 43 },
    { id: 2, alt: "Dalmatyńczyk", filename: "obraz3.jpg", category: 2, downloads: 2 },
    { id: 3, alt: "Świnka morska", filename: "obraz4.jpg", category: 2, downloads: 53 },
    { id: 4, alt: "Rotwailer", filename: "obraz5.jpg", category: 2, downloads: 43 },
    { id: 5, alt: "Audi", filename: "obraz6.jpg", category: 3, downloads: 11 },
    { id: 6, alt: "kotki", filename: "obraz7.jpg", category: 2, downloads: 22 },
    { id: 7, alt: "Róża", filename: "obraz8.jpg", category: 1, downloads: 33 },
    { id: 8, alt: "Świnka morska", filename: "obraz9.jpg", category: 2, downloads: 123 },
    { id: 9, alt: "Foksterier", filename: "obraz10.jpg", category: 2, downloads: 22 },
    { id: 10, alt: "Szczeniak", filename: "obraz11.jpg", category: 2, downloads: 12 },
    { id: 11, alt: "Garbus", filename: "obraz12.jpg", category: 3, downloads: 321 },
];

const Galeria = () => {
    const [categories, setCategories] = useState({ 1: true, 2: true, 3: true });
    const [data, setData] = useState(initialData);

    const toggleCategory = (category) => {
        setCategories((prev) => {
            const updatedCategories = { ...prev };
            if (updatedCategories[category]) {
                updatedCategories[category] = false;
            } else {
                updatedCategories[category] = true;
            }
            return updatedCategories;
        });
    };

    const increment = (id) => {
        setData((prevData) => {
            const updatedData = [...prevData];
            const item = updatedData.find((item) => item.id === id);
            if (item) item.downloads += 1;
            return updatedData;
        });
    };

    return (
        <>
            <h1>Kategorie zdjęć</h1>
            <div className="form-check form-switch d-flex justify-content-between">
                <label className="form-check-label">
                    <input className="form-check-input" type="checkbox" role="switch" checked={categories[1]}
                           onChange={() => toggleCategory(1)}/>
                    Kwiaty
                </label>
                <label className="form-check-label">
                    <input className="form-check-input" type="checkbox" role="switch" checked={categories[2]}
                           onChange={() => toggleCategory(2)}/>
                    Zwierzęta
                </label>
                <label className="form-check-label">
                    <input className="form-check-input" type="checkbox" role="switch" checked={categories[3]}
                           onChange={() => toggleCategory(3)}/>
                    Samochody
                </label>
            </div>


            <div className="grid-container">
                {data
                    .filter((item) => categories[item.category])
                    .map((item) => (
                        <div key={item.id} className="grid-item">
                            <img src={item.filename} alt={item.alt}/>
                            <h4>Pobrań: {item.downloads}</h4>
                            <button
                                type="button"
                                className="btn btn-success"
                                onClick={() => increment(item.id)}
                            >
                                Pobierz
                            </button>
                        </div>
                    ))}
            </div>
        </>
    );
};

export default Galeria;
