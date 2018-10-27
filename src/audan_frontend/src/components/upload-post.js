import React from 'react';
import Dropzone from 'react-dropzone';
import Request from 'superagent';
import { Progress } from 'reactstrap';

class UploadPost extends React.Component {
  constructor() {
    super()
    this.state = {
        files: [],
        progress: "0%",
        uploading: false,
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
          console.log(err);
          console.log(res);
      })
    this.setState({
      files
    });
  }

  render() {
    return (
      <section style={{marginLeft: '250px', marginTop: '100px'}}>
        <div className="dropzone" >
          <Dropzone multiple={false} accept='video/*' onDrop={this.onDrop.bind(this)}>
            <p>Drop a video here, or click to select video to upload.</p>
          </Dropzone>
        </div>
        <aside>
          <h2>Dropped files</h2>
          <ul>
            {
              this.state.files.map((f, ind) => <li key={ind}>{f.name} - {f.size} bytes</li>)
            }
          </ul>
        </aside>
        <div className="text-center">{`${this.state.progress}`}</div>
        {this.state.uploading ? <Progress value={this.state.progress} /> : null}
      </section>
    );
  }
}

export default UploadPost