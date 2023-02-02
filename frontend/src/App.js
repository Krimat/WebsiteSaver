import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'
import './App.css';
import {Input, Button} from 'reactstrap'
import {useState} from 'react'

import Grid from './components/Grid'
import { useEffect } from 'react';

import defaultImage from './noImage.jpg'


function App() {
  const sitesLink = 'api/sites/'
  const [searchInput, setSearchInput] = useState('');
  const [nextPageLink, setNextPageLink] = useState(null);
  const [prevPageLink, setPrevPageLink] = useState(null);
  const [sites, setSites] = useState([]);


  const handleOnChange = (event) => {
    setSearchInput(event.target.value);
  }

  const updateSites = (link) => {
    axios.get(link).then((result)=>{
      setSites(result.data.results)
      console.log(result, sites);
      setNextPageLink(result.data.next);
      setPrevPageLink(result.data.previous);
    })
  }

  const handleOnKeyDown = (event) => {
    if (event.key === "Enter") {
      updateSites(sitesLink + "?name=" + searchInput)
    }
  }

  useEffect(() => {
    updateSites(sitesLink);
  }, []);

  return (
    
    <>
      <div className='navbar bg-dark text-light'>
        WebsiteSaver
      </div>

      <div className='d-flex justify-content-center m-3'>
        <Input
        className='w-25'
        onChange={handleOnChange}
        onKeyDown={handleOnKeyDown}
        />
        <Button
        onClick={()=>updateSites(sitesLink + "?name=" + searchInput)}
        >
          Search
        </Button>
      </div>
      {sites !== [] ? (
        <Grid
      sites={sites}
      defaultImage={defaultImage}
      colNumber={5}
      />
      ): (
        <div className='d-flex justify-content-center'>
          Found nothing with given search paramentrs name:{searchInput}
        </div>
      )}
      

      
      <div>
        <div className='d-flex justify-content-center mt-2'>
          <Button
          disabled={prevPageLink === null}
          onClick={()=>updateSites(prevPageLink)}
          >
            Prev
          </Button>
          <Button
          disabled={nextPageLink === null}
          onClick={()=>updateSites(nextPageLink)}
          >
            Next
          </Button>
        </div>
        
      </div>



    </>
  );
}

export default App;
