import React from 'react';
// import footerLogo from '../../assets/images/footerlogo2.png'
import './footer.css';

const Footer = () => {
  return (
      <div className="footer p-3">
        {/* <a className="logo" href="http://www.cnergres.iitkgp.ac.in/aclakg/">
          <img src={footerLogo} alt="Logo"/>
        </a> */}
        <p>
          Developed by Dhiraj Barnwal, Dibya Prakash Das, Rahul Vernwal, Sayan Sinha for Hack-a-Bit
          <br />
          {/*Copyright © <a href="http://www.iitkgp.ac.in"> IIT Kharagpur</a> and*/}
          {/*<a href="http://www.cnergres.iitkgp.ac.in/"> CNERG Research Group</a>*/}
        </p>
      </div>
  )
}

export default Footer;
