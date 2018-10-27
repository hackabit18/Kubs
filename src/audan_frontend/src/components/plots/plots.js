import React, {Component} from 'react'
import Plot from 'react-plotly.js';
import {Container, Row, Col} from 'reactstrap';

class Plots extends Component {
  render() {
    return (
      <Container className="about py-1">
        <Row>
          <Col>
            <Plot
              data={[this.props.data]}
              layout={ {width: 800, height: 600 , title: 'A Fancy Plot'} }
            />
          </Col>
          <Col>
            <p>something</p>
          </Col>
        </Row>
      </Container>

    )
  }
}

export default Plots
