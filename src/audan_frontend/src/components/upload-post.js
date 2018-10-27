import React from 'react';
import Dropzone from 'react-dropzone';
import Request from 'superagent';
import { Progress } from 'reactstrap';

import PreLoader from './preloader/preloader';

class UploadPost extends React.Component {
  constructor() {
    super()
    this.state = {
        files: [],
        progress: "0%",
        uploading: false,
        loading: false,
    }
  }

  /*We will be using Request.post() to the send our post request
  "http://posttestserver.com/post.php?dir=example" was used for testing our post request
  '.set' is where we give our headers
  '.send' is where we attach the file that is to be sent
  * '.attach' can also be used to send a fil
  '.on' is used to find out the progress of the file upload
  For demonstration purpose we just show the value of percentage complete
  The value can be passed to progress bar and can also be used to calculate time remaining*/
  onDrop(files) {
    this.setState({uploading: true})
    Request.post('/upload_video')
    //   .type('form')
      .attach('file', files[0])
    //   .send(files[0])
      .on('progress', function(e) {
        this.setState({progress: e.percent + "%"})
      }.bind(this))
      .on('error', function(e){
        this.setState({progress: "Cannot connect to Server!"})
      }.bind(this))
      .end((err, res) => {
          if(err) {
            console.log(err)
          }
          if(res.body.success) {
            this.setState({loading: true})
          }
      })
      this.setState({files});
  }

  render() {
    return (
      <div className="dropzone">

        { this.state.loading ?
          <PreLoader />
          :
          (
          <div>
            <h2 className="upload_name">Upload your video here</h2>

            <div>
              <Dropzone className="dropzone_component"  multiple={false} accept='video/*' onDrop={this.onDrop.bind(this)}>
                <p>Drop a video here, or click to select video to upload.</p>
              </Dropzone>
            </div>

            <div>
            {this.state.uploading ?
              <h5 style={{"padding": "5%"}} >Dropped files</h5> : null }
              <ul>
                {
                  this.state.files.map((f, ind) => <li key={ind}>{f.name} - {f.size} bytes</li>)
                }
              </ul>
            </div>


            {this.state.uploading ?
              (
                <div>
                  <div className="text-center">File Upload {`${this.state.progress}`} </div>
                  <Progress value={this.state.progress.substring(0, this.state.progress.length - 1)} />
                </div> )
              : null
            }
          </div>
          )}
      </div>
    );
  }
}

export default UploadPost;
