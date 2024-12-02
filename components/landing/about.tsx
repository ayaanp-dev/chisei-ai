import { Button } from "@/components/ui/button"
import Image from "next/image"

export function About() {
  return (
    <section id="about" className="py-20 bg-background">
      <div className="container mx-auto px-4">
        <div className="flex flex-col lg:flex-row items-center gap-12">
          <div className="lg:w-1/2">
            <Image
              src="/placeholder.svg?height=400&width=600"
              alt="Chisei AI Team"
              width={600}
              height={400}
              className="rounded-lg shadow-lg"
            />
          </div>
          <div className="lg:w-1/2 space-y-6">
            <h2 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">About Chisei AI</h2>
            <p className="text-lg text-muted-foreground">
              At Chisei AI, we're passionate about revolutionizing the way students learn. Our team of educators, AI experts, and software engineers came together with a shared vision: to harness the power of artificial intelligence to create a more efficient, effective, and personalized learning experience.
            </p>
            <p className="text-lg text-muted-foreground">
              Founded in 2023, we've been on a mission to develop cutting-edge AI tools that adapt to each student's unique learning style and needs. Our platform is designed to not just help students memorize information, but to truly understand and engage with their studies.
            </p>
            <Button size="lg" className="bg-purple-600 hover:bg-purple-700">Learn More About Our Mission</Button>
          </div>
        </div>
      </div>
    </section>
  )
}

