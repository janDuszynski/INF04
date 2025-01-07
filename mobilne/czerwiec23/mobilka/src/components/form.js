import { useState } from "react";
import "./style.css";
import "bootstrap/dist/css/bootstrap.css";

export default function Form() {
  const [tytul, setTytul] = useState("");
  const [rodzaj, setRodzaj] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Tytuł: ${tytul}; Rodzaj: ${rodzaj}`);
  };
  return (
    <>
      <form onSubmit={handleSubmit} class="form-group">
        Tytuł Filmu <br />
        <input
          type="title"
          value={tytul}
          class="form-control"
          onChange={(e) => setTytul(e.target.value)}
        />{" "}
        <br />
        Rodzaj <br />
        <select
          class="form-control"
          name="Rodzaj"
          id="Rodzaj"
          value={rodzaj}
          onChange={(e) => setRodzaj(e.target.value)}
        >
          <option value={null}></option>
          <option value="1">Komedia</option>
          <option value="2">Obyczajowy</option>
          <option value="3">Sensacyjny</option>
          <option value="4">Horror</option>
        </select>
        <br />
        <button class="btn btn-success" name="submit" type="submit">
          Dodaj
        </button>
      </form>
    </>
  );
}
