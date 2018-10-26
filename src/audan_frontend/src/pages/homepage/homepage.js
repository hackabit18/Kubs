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
      <div>
        <div className='header'>
          <Navbar color="faded" light toggleable>
            <NavbarToggler right onClick={this.toggle} />
            <NavbarBrand href="/">
              <p>AudAn</p>
            </NavbarBrand>
            <Collapse isOpen={this.state.isOpen} navbar>
              <Nav className="p-2" navbar>
                <NavItem>
                  <NavLink href="/aclakg">Home</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/aclakg/search">Search</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/aclakg/team">The Team</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/aclakg/contact">Contact Us</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/aclakg/about">About Us</NavLink>
                </NavItem>
                <NavItem>
                  <NavLink href="/aclakg/api">API</NavLink>
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