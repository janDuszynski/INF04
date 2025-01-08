import {useState} from 'react'
import 'bootstrap/dist/css/bootstrap.css'

function OnlyOneComponent() {
    const courses = ["Programowanie w C#", "Angular dla początkujących", "Kurs Django"]

    const [name, setName] = useState('')
    const [course, setCourse] = useState('')

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(`${name}`)
        if (course < 1 || course > courses.length)
        {
            console.log("Nieprawidłowy numer kursu")
        }
        else
        {
            console.log(`${courses[course-1]}`)
        }
    }

    return (
        <>
            <h2>Liczba kursów: {courses.length}</h2>
            <ol>
                {courses.map((course, index) => (
                    <li key={index}>{course}</li>
                ))}
            </ol>
            <form className="form-group" onSubmit={handleSubmit}>
                <label htmlFor="name">
                    Imię i nazwisko:<br/>
                    <input type="text" name="name" className="form-control" value={name} onChange={(e) => {setName(e.target.value)}}/>
                </label><br/>
                <label htmlFor="course">
                    Numer kursu:<br/>
                    <input type="number" name="course" className="form-control" value={course} onChange={(e) => {setCourse(e.target.value)}}/>
                </label><br/>
                <button type="submit" className="btn btn-success">Zapisz do kursu</button>
            </form>
        </>
    );
}

export default OnlyOneComponent;
