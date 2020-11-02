import React, { Component } from 'react';

class StarshipPage extends Component {
  state = {
    mylist: []
  }
  componentDidMount() {
    fetch('http://localhost:5500/api/v1/starships')
    .then(res => res.json())
    .then((data) => {
      this.setState({ mylist: data })
      //console.log(this.state.mylist)
    })
    .catch(console.log)
  }
  render() {
    return (
      <div className="container">
        <div className="col-xs-12">
        <h1>Starships within 30 parsecs</h1>
          {this.state.mylist.map((acc) => (
            <div className="card">
            <div className="card-body">
              <h5 className="card-title">{acc.name} {acc.registry}</h5>
              <h6 className="card-subtitle mb-2">
                RA:{acc.lastknownpositionra},DEC:{acc.lastknownpositiondec},Distance:{acc.lastknownpositiondistance}
              </h6>
              <h6 className="card-subtitle mb-2 text-muted">
                {acc.significance}
              </h6>
            </div>
          </div>
        ))}~
      </div>
     </div>
    );
  }
}

export default StarshipPage;
