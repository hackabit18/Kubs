import React, {Component} from 'react'
import Plot from 'react-plotly.js';
import Request from 'superagent';
import './plots.css'
import {Container, Row, Col, Button} from 'reactstrap';

class Plots extends Component {
  constructor() {
    super()

    this.state = {
      personData: null,
    }
    this.personData = this.personData.bind(this)
  }

  personData() {
    // var data1 = {"face_4":{
    //   "emotion":"surprised",
    //   "age":6.0
    //      },
    //      "face_5":{
    //         "emotion":"sad",
    //         "age":28.0
    //      },
    //      "face_1":{
    //         "emotion":"surprised",
    //         "age":10.0
    //      },
    //      "face_2":{
    //         "emotion":"surprised",
    //         "age":9.0
    //      },
    //      "face_3":{
    //         "emotion":"surprised",
    //         "age":7.0
    //      }
    //   }
    //   var personArray = [];
    //    for (var key in data1) {
    //      personArray.push(
    //        <Col>
    //          <h3>Reaction: {data1[key]['emotion']}</h3>
    //          <h4>Age: {data1[key]['age']}</h4>
    //        </Col>
    //      )
    //    }
    //    this.setState({personData: personArray})

    Request
    .get('/personData')
    .then(res => {
       console.log(res.body)
       var personArray = [];
       for (var key in res.body) {
         personArray.push(
           <Col>
             <h3>Reaction: {res.body[key]['emotion']}</h3>
             <h3>Age: {res.body[key]['age']}</h3>
           </Col>
         )
       }
       this.setState({personData: personArray})
    })
    .catch(err => {
       console.log(err)
    });
  }

  render() {
    return (
      <Container className="plots py-1">
        <Row className="initial-stats py-5">
          <Col xs="12" md="4">
            <div className="stat-box">
              <h1>{parseFloat(this.props.data.surprise_per).toFixed(2)}%</h1>
              <p>on average were surprised</p>
            </div>
          </Col>
          <Col xs="12" md="4">
            <div className="stat-box">
              <h1>{parseFloat(this.props.data.sad_per).toFixed(2)}%</h1>
              <p>on average were sad</p>
            </div>
          </Col>
          <Col xs="12" md="4">
            <div className="stat-box">
              <h1>{parseFloat(this.props.data.happy_per).toFixed(2)}%</h1>
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
        <Row>
          <Button style={{ margin: '0 auto', marginBottom: '30px'}} onClick={this.personData} color="primary" size="lg">Get Person to Person Data</Button>
          {this.state.personData}
        </Row>
      </Container>

    )
  }
}

export default Plots
