"use client";
import React from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { ModeToggle } from "@/components/mode-toggle";
import { cn } from "@/lib/utils";

export function NavbarComponent() {
  return (
    <div className="w-full flex justify-center p-4 sticky top-0 z-50">
      <div className="max-w-5xl w-full border border-zinc-200 dark:border-zinc-800 rounded-lg bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="flex h-16 items-center justify-between px-4">
          {/* Left side - Logo and Navigation */}
          <div className="flex items-center gap-8">
            {/* Logo and Company Name */}
            <Link href="/" className="flex items-center gap-2">
              {/* Replace with your actual logo */}
              <div className="h-8 w-8 rounded-full bg-primary"></div>
              <span className="text-xl font-bold">Chisei AI</span>
            </Link>

            {/* Navigation Links */}
            <nav className="flex items-center gap-6">
              <Link 
                href="/about"
                className="text-sm font-medium hover:text-primary transition-colors"
              >
                About
              </Link>
              <Link 
                href="/faq"
                className="text-sm font-medium hover:text-primary transition-colors"
              >
                FAQ
              </Link>
              <Link 
                href="/blog"
                className="text-sm font-medium hover:text-primary transition-colors"
              >
                Blog
              </Link>
              <Link 
                href="https://github.com/your-repo"
                className="text-sm font-medium hover:text-primary transition-colors"
                target="_blank"
                rel="noopener noreferrer"
              >
                GitHub
              </Link>
            </nav>
          </div>

          {/* Right side - Auth Buttons and Theme Toggle */}
          <div className="flex items-center gap-4">
            <Button variant="ghost" asChild>
              <Link href="/signin">Sign In</Link>
            </Button>
            <Button variant="ghost" asChild>
              <Link href="/signup">Sign Up</Link>
            </Button>
            <Button variant="default" asChild>
              <Link href="/get-started">Get Started</Link>
            </Button>
            <ModeToggle />
          </div>
        </div>
      </div>
    </div>
  );
}