import {useState,useEffect} from "react"
import {getPosts} from './Api';
import './App.css';
import Company from "./components/company";

function App() {

  const [data, setData] = useState(null);

  useEffect(() => {
    getPosts().then((posts) => setData(posts));
  }, []);

  return( <div className="App">
    {
      data ? data.map(e => <Company name={e.name} about={e.about} location={e.location} type={e.type}/>) : <p>No data</p>
    }
  </div>
  )
}

export default App;
