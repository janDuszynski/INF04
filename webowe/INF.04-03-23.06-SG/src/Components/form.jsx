import {useState} from 'react'
import 'bootstrap/dist/css/bootstrap.css';

function FormSupreme() {
    const [title, setTitle] = useState('')
    const [filmtype, setFilmType] = useState('')

    const handleSumbit = (e) => {
        e.preventDefault()
        console.log(`title: ${title}, rodzaj: ${filmtype}`)
    }
  return (
    <>
        <form onSubmit={handleSumbit} className="form-group">
            <label htmlFor="title">
                Tytuł filmu<br/>
                <input type="text" name="title" className="form-control" value={title}
                       onChange={(e) => setTitle(e.target.value)}/>
            </label><br/>
            <label htmlFor="filmtype">
                Rodzaj<br/>
                <select name="filmType" className="form-control" value={filmtype}
                        onChange={(e) => setFilmType(e.target.value)}>
                    <option value={null}></option>
                    <option value="1">Komedia</option>
                    <option value="2">Obyczajowy</option>
                    <option value="3">Sensacyjny</option>
                    <option value="4">Horror</option>
                </select>
            </label><br/><br/>
            <button type="submit" className="btn btn-success">Dodaj</button>
        </form>
    </>
  );
}

export default FormSupreme;