import React, {Component} from 'react';
import {Container, Row, Col} from 'reactstrap';
import UploadPost from '../upload-post';
import './upload.css';

export default class Upload extends Component {
  render() {
    return (
      <Container fluid className="stats py-5">
        <Container className="py-3">
          <Row>
              <h3>Upload your video here</h3>
              <UploadPost />
          </Row>
        </Container>
      </Container>
    );
  }
}