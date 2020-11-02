import React from "react";
import {Link} from "react-router-dom";

function Navbar() {
    return (
        <div>
        <Link to="/">Home </Link><br/>
        <Link to="/starships">Starships </Link><br/>
        <Link to="/localstars">Local Stars</Link>
        </div>
    );
};

export default Navbar;