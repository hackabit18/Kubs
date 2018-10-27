import React, {Component} from 'react';
import {Container, Row, Col} from 'reactstrap';

export default class About extends Component {
  render() {
    return (
      <Container fluid className="about">
        <Container className="py-1">
          <h1>How it Works</h1>
          <Row>
            <Col>
              <img alt='sample' src={require('../assets/video-player.png')} />
              <div className='desc'>Video in uploaded as input</div>
            </Col>
            <Col>
              <img alt='sample' src={require('../assets/albums.png')} />
              <div className='desc'>Video gets converted into image frames</div>
            </Col>
            <Col>
              <img alt='sample' src={require('../assets/research.png')} />
              <div className='desc'>Cognitive tools are used to analyze faces</div>
            </Col>
            <Col>
              <img alt='sample' src={require('../assets/analysis.png')} />
              <div className='desc'>A brief report describes our data</div>
            </Col>
          </Row>
        </Container>
      </Container>
    );
  }
}
