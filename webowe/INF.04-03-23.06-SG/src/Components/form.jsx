import { useState } from "react";

function Form() {
    const [list, useList] = useState(['', 'Komedia o wartości 1', 'Obyczajowy o wartości 2', 'Sensacyjny o wartości 3', 'Horror o wartości 4']);
    const [title, setTitle] = useState('');
    const [genere, setGenere] = useState('');

    const handleChange = (e) => {
        e.preventDefault();
        console.log(`tytul: ${title}; rodzaj: ${genere}`)
    }
    
  return (

    <form onSubmit={handleChange}>
        <div className="form-group">
            <label>Tytuł filmu</label>
            <input type="text" className="form-control" onChange={(e) => setTitle(e.target.value)}/> <br/>

            <label>Rodzaj</label>
            <select className="form-control" value={genere} onChange={(e) => setGenere(e.target.value)} >
            {list.map((value, index) => (
                <option key={index} value={value}>
                {value}
                </option>
            ))}
            </select>
            <button type="submit" className="btn btn-success">Dodaj</button>
        </div>
    </form>
  );
}

export default Form;
