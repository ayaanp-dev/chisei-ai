import { Button } from "@/components/ui/button"
import Image from "next/image"

export function Hero() {
  return (
    <section className="relative py-20 overflow-hidden">
      <div className="absolute inset-0 z-0">
        <Image
          src="/placeholder.svg?height=600&width=1200"
          alt="AI Study Background"
          layout="fill"
          objectFit="cover"
          quality={100}
          className="opacity-10"
        />
      </div>
      <div className="container mx-auto px-4 relative z-10">
        <div className="flex flex-col lg:flex-row items-center gap-12">
          <div className="lg:w-1/2 space-y-8">
            <h1 className="text-5xl md:text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
              Revolutionize Your Study Habits with AI
            </h1>
            <p className="text-xl md:text-2xl text-muted-foreground">
              Chisei AI empowers students to learn smarter, not harder. Summarize notes, generate practice questions, and optimize your study schedule with the power of artificial intelligence.
            </p>
            <div className="flex flex-col sm:flex-row gap-4">
              <Button size="lg" className="text-lg bg-purple-600 hover:bg-purple-700">
                Get Started Free
              </Button>
              <Button size="lg" variant="outline" className="text-lg">
                Watch Demo
              </Button>
            </div>
          </div>
          <div className="lg:w-1/2">
            <div className="relative w-full aspect-square">
              <Image
                src="/placeholder.svg?height=600&width=600"
                alt="Chisei AI Interface"
                layout="fill"
                objectFit="contain"
                className="rounded-lg shadow-2xl"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

