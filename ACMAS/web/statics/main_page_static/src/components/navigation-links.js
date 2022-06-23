import React from 'react'

import PropTypes from 'prop-types'

import './navigation-links.css'

const NavigationLinks = (props) => {
  return (
    <nav className={`navigation-links-nav ${props.rootClassName} `}>
      <span className="navigation-links-text">{props.text}</span>
      <span className="navigation-links-text1">{props.text1}</span>
      <span className="navigation-links-text2">{props.text2}</span>
      <span className="navigation-links-text3">{props.text3}</span>
      <span className="navigation-links-text4">{props.text4}</span>
    </nav>
  )
}

NavigationLinks.defaultProps = {
  text1: 'Features',
  text4: 'Blog',
  rootClassName: '',
  text3: 'Team',
  text: 'About',
  text2: 'Pricing',
}

NavigationLinks.propTypes = {
  text1: PropTypes.string,
  text4: PropTypes.string,
  rootClassName: PropTypes.string,
  text3: PropTypes.string,
  text: PropTypes.string,
  text2: PropTypes.string,
}

export default NavigationLinks
