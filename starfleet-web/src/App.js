import React from "react";

import Landing from "./components/Landing"
import Notfound from "./components/NotFound"
import StarshipPage from "./components/StarshipPage"
import LocalStarPage from "./components/LocalStarPage"
import Navbar from "./components/Navbar"

import { BrowserRouter , Switch, Route} from 'react-router-dom';

function App() {
    return (     
        <main>
           <Navbar/>
            <Switch>
                <Route path="/" component={Landing} exact />
                <Route path="/starships" component={StarshipPage} />
                <Route path="/localstars" component={LocalStarPage} />
                <Route component={Notfound} />
            </Switch>
        </main>
    )
}

export default App;
