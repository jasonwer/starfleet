import React, { Component } from 'react';

class LocalStarPage extends Component {
  state = {
    mylist: []
  }
  componentDidMount() {
    fetch('http://localhost:5501/api/v1/localstars')
    .then(res => res.json())
    .then((data) => {
      this.setState({ mylist: data })
      console.log(this.state.mylist)
    })
    .catch(console.log)
  }
  render() {
    return (
      <div className="container">
        <div className="col-xs-12">
        <h1>Local stars</h1>
          {this.state.mylist.map((acc) => (
            <div className="card">
            <div className="card-body">
              <h5 className="card-title">{acc.name}</h5>
              <h5 className="card-title">{acc.common_name}</h5>
              <h5 className="card-title">{acc.mass}</h5>
              <h5 className="card-title">{acc.distance_ly}</h5>
            </div>
          </div>
        ))}~
      </div>
     </div>
    );
  }
}

export default LocalStarPage;
