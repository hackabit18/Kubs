import React, {Component} from 'react';
import Upload from '../../components/upload/upload';
import { Collapse, Navbar, NavbarToggler, NavbarBrand, Nav, NavItem, NavLink, Jumbotron } from 'reactstrap';
import './homepage.css';

export default class Homepage extends Component {

  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false,
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }

  render() {
    return (
      <div className='home-jumbo'>
        <div className='header'>
          <Navbar color="faded" light toggleable>
            <NavbarToggler right="true" onClick={this.toggle} />
            <NavbarBrand href="/">
              <p>AudAn</p>
            </NavbarBrand>
            <Collapse isOpen={this.state.isOpen} navbar>
              <Nav className="p-2" navbar>
                <NavItem>
                  <NavLink href="/">Home</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/team">The Team</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/contact">Contact Us</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/about">About Us</NavLink>
                </NavItem>
              </Nav>
            </Collapse>
          </Navbar>
        </div>
        <Jumbotron className="search-container">
          <h1 className="display-5">AUDience ANalysis</h1>
          <p className="lead">
            A Fully Automated platform to analyze your audience
           </p>
          <div>
              <p>Some content to be added here</p>
          </div>
        </Jumbotron>
        <Upload />
      </div>
    );
  }
}
