import React from 'react'

import PropTypes from 'prop-types'

import './navigation-links1.css'

const NavigationLinks1 = (props) => {
  return (
    <nav className={`navigation-links1-nav ${props.rootClassName} `}>
      <span className="navigation-links1-text">{props.text}</span>
      <span className="navigation-links1-text1">{props.text1}</span>
      <span className="navigation-links1-text2">{props.text2}</span>
      <span className="navigation-links1-text3">{props.text3}</span>
      <span className="navigation-links1-text4">{props.text4}</span>
    </nav>
  )
}

NavigationLinks1.defaultProps = {
  text: 'About',
  text3: 'Team',
  text2: 'Pricing',
  text1: 'Features',
  text4: 'Blog',
  rootClassName: '',
}

NavigationLinks1.propTypes = {
  text: PropTypes.string,
  text3: PropTypes.string,
  text2: PropTypes.string,
  text1: PropTypes.string,
  text4: PropTypes.string,
  rootClassName: PropTypes.string,
}

export default NavigationLinks1
