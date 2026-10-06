import { useState } from 'react'


const Form = () => {
    const [courses, setCourses] = useState(['Programowanie w C#', 'Angular dla początkujących', 'Kurs Django'])
    const [userData, setUserData] = useState('')
    const [courseNumber, setCourseNumber] = useState('')


    const handleSubmit = (e) => {
        e.preventDefault()
        console.log(userData)
        console.log(courseNumber)
    }
    const handleCourseChange = (e) => {
        let value = parseInt(e.target.value)
        if (value > 0 && value <= courses.length){
            setCourseNumber(courses[value - 1])
        }
        else{
            setCourseNumber(" Nieprawidłowy numer kursu")
        }


    }
    return (
        <>
            <h2>Liczba kursów: {courses.length}</h2>
            <ol>
                {courses.map((course, i) => (<li key={i}>{course}</li>))}
            </ol>

            <form className="form-group" onSubmit = {(e) => handleSubmit(e)}>
                <label htmlFor="userData">Imię i nazwisko</label><br/>
                <input type="text" id="userData" className="form-control" onChange={e => {setUserData(e.target.value)}}/><br/>
                <label htmlFor="courseNumber">Numer kursu</label><br/>
                <input type="text" id="courseNumber" className="form-control" onChange={e => {handleCourseChange(e)} }/> <br/>
                <button type="submit" className="btn btn-success">Zapisz się do kursu</button>
            </form>
        </>
    )
}

export default Form
