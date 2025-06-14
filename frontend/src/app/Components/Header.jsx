'use client'
import { SignInButton, UserButton } from '@clerk/nextjs'
import Image from 'next/image'
import Link from 'next/link'
import React from 'react'



function Header() {
  return (
    <>
    <header className='bg-white'>
        <div className='flex justify-between mx-auto py-4 w-[90%]'>
            <div className='flex align-center gap-4'>
                <div className='logo'><Image 
        src="/images/logo1.png" 
        alt="Logo" 
        width={50} 
        height={20} 
      /></div>
                <div className='flex font-'>AgniRakshak</div>
            </div>
            <div className=''>
                <UserButton/></div>                
            </div>

        
    </header>
      
    </>
  )
}

export default Header
