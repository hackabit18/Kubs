import React, {Component} from 'react';
// import SearchBar from '../../components/search-bar-homepage/search-bar-homepage';
// import About from '../../components/about/about';
// import Stats from '../../components/stats/stats';
// import Graphs from '../../components/graphs/graphs';
import { Jumbotron } from 'reactstrap';
import './homepage.css';

export default class Homepage extends Component {
  render() {
    return (
      <div>
        <Jumbotron className="search-container">
          <h1 className="display-5">AUDience ANalysis</h1>
          <p className="lead">
            A Fully Automated platform to analyze your audience
           </p>
          <div>
              <p>Some content to be added here</p>
          </div>
        </Jumbotron>
      </div>
    );
  }
}