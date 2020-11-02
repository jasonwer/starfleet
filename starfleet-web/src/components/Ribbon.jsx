import React, { Component} from 'react';
import PropTypes from 'prop-types';
import IconText from './IconText';

export default class Ribbon extends Component {
  static contextTypes = {
    router: PropTypes.object.isRequired
  }
  constructor(props) {
    super(props);
    this.state = { ribbonActive: '' };
  }
  setRibbonActive(activeText) {
    this.setState({ ribbonActive: activeText });
    //this.context.router.history.push(activeText.toLowerCase());
    //this.context.history.push(activeText.toLowerCase());
    var abc = this.context.history;
  }
  render() {
    return (
      <section className="ribbon">
        <IconText
          onClick={this.setRibbonActive.bind(this, 'StarshipPage')}
          active={this.state.ribbonActive === 'starships'}
          ribbon text="Starshipsss" icon="list-alt"
          size="2x" className="default" />
        <IconText
          onClick={this.setRibbonActive.bind(this, 'LocalStarPage')}
          active={this.state.ribbonActive === 'localstars'}
          ribbon text="Local stars" icon="cloud"
          size="2x" className="default" />
      </section>
    );
  }
}

