import React, {Component} from 'react'
import Plot from 'react-plotly.js';
import './plots.css'
import {Container, Row, Col} from 'reactstrap';

class Plots extends Component {
  render() {
    return (
      <Container className="plots py-1">
        <Row className="initial-stats py-5">
          <Col xs="12" md="4">
            <div className="stat-box">
              <h1>42%</h1>
              <p>on average were surprised</p>
            </div>
          </Col>
          <Col xs="12" md="4">
            <div className="stat-box">
              <h1>21.6%</h1>
              <p>Ton average were sad</p>
            </div>
          </Col>
          <Col xs="12" md="4">
            <div className="stat-box">
              <h1>28.2%</h1>
              <p>on average were happy</p>
            </div>
          </Col>
        </Row>
        <Row>
          <Col xs="6">
            <Plot
              data={[{
                x:this.props.data.time,
                y: this.props.data.sadness,
                z: this.props.data.surprise,
                mode: 'markers',
                marker: {
                  size: 3,
                  line: {
                  color: 'rgba(217, 217, 217, 0.14)',
                  width: 0.5},
                  opacity: 0.8},
                type: 'scatter3d'
              }]}
              layout={ {	scene: {
                xaxis:{title: 'Time'},
                yaxis:{title: 'Sadness'},
                zaxis:{title: 'Surprise'},
                },
                width: 550, height: 600 , title: 'Time vs Sadness vs Surprise'} }
            />
          </Col>
          <Col xs="6">
            <Plot
              data={[{
                x:this.props.data.time,
                y: this.props.data.sadness,
                mode: 'lines',
                name: 'Sadness',
              },
              {
                x:this.props.data.time,
                y: this.props.data.surprise,
                mode: 'lines',
                name: 'Surprise',
              },
              {
                x:this.props.data.time,
                y: this.props.data.happiness,
                mode: 'lines',
                name: 'Happiness',
              }
            ]}
              layout={{width: 550, height: 600 , title: 'Time vs Emotions'} }
            />
          </Col>
        </Row>
      </Container>

    )
  }
}

export default Plots
