import { Navbar } from "@/components/landing/navbar"
import { Hero } from "@/components/landing/hero"
import { Features } from "@/components/landing/features"
import { Testimonials } from "@/components/landing/testimonials"
import { About } from "@/components/landing/about"
import { Contact } from "@/components/landing/contact"
import { Footer } from "@/components/footer"
import { Bottom } from "@/components/landing/bottom"

export default function LandingPage() {
  return (
    <div className="min-h-screen flex flex-col bg-background text-foreground">
      <Navbar />
      <main>
        <Hero />
        <Features />
        <Testimonials />
        <Bottom />
      </main>
      <Footer />
    </div>
  )
}