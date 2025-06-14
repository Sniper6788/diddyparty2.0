import { SignInButton, UserButton } from '@clerk/nextjs'
import Link from 'next/link'
import React from 'react'

function Header() {
  return (
    <>
    <header>
        <div className='flex justify-between mx-auto py-2 w-[90%]'>
            <div className='flex'>
                <div className='logo-img'></div>
                <div className=''>AgniRakshak</div>
            </div>
            <div className=''>
                <SignInButton/></div>                
            </div>

        
    </header>
      
    </>
  )
}

export default Header
