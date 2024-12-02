import Link from "next/link"
import { BookOpen } from 'lucide-react'

export function Footer() {
  return (
    <footer className="bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 border-t border-purple-500/20 py-12">
      <div className="container mx-auto px-4">
        <div className="flex flex-wrap justify-between">
          <div className="w-full md:w-1/4 mb-8 md:mb-0">
            <Link href="/" className="flex items-center space-x-2 mb-4">
              <BookOpen className="h-6 w-6 text-purple-500" />
              <span className="font-bold text-xl">Chisei AI</span>
            </Link>
            <p className="text-muted-foreground">
              Empowering students with AI-driven study tools for a smarter learning experience.
            </p>
          </div>
          <div className="w-full md:w-1/4 mb-8 md:mb-0">
            <h3 className="font-bold text-lg mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Home</Link></li>
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Features</Link></li>
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">About Us</Link></li>
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Contact</Link></li>
            </ul>
          </div>
          <div className="w-full md:w-1/4 mb-8 md:mb-0">
            <h3 className="font-bold text-lg mb-4">Legal</h3>
            <ul className="space-y-2">
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Terms of Service</Link></li>
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Privacy Policy</Link></li>
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Cookie Policy</Link></li>
            </ul>
          </div>
          <div className="w-full md:w-1/4">
            <h3 className="font-bold text-lg mb-4">Connect With Us</h3>
            <ul className="space-y-2">
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Twitter</Link></li>
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Facebook</Link></li>
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">LinkedIn</Link></li>
              <li><Link href="#" className="text-muted-foreground hover:text-purple-400">Instagram</Link></li>
            </ul>
          </div>
        </div>
        <div className="border-t border-purple-500/20 mt-8 pt-8 text-center">
          <p className="text-muted-foreground">© 2023 Chisei AI. All rights reserved.</p>
        </div>
      </div>
    </footer>
  )
}