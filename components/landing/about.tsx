import { Button } from "@/components/ui/button"
import Image from "next/image"

export function About() {
  return (
    <section id="about" className="py-20 bg-background border-t border-purple-500/20">
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
              Hey, I'm Ayaan! I'm the founder and developer of Chisei AI. I'm a high school student who's passionate about technology and education. I created Chisei AI to help students like me study smarter, not harder. I believe that AI has the power to revolutionize the way we learn, and I'm excited to be at the forefront of that change.
            </p>
            <p className="text-lg text-muted-foreground">
              Founded in 2024, I admitedally started Chisei AI for me. I was struggling to keep up with my schoolwork and I knew there had to be a better way. I started experimenting with AI and machine learning, and I quickly realized the potential for these technologies to transform the way we study. I built Chisei AI to help students summarize complex notes, generate custom questions, optimize study schedules, and track their progress. I'm proud to say that Chisei AI has helped thousands of students around the world study more efficiently and effectively.
            </p>
            <Button size="lg" className="bg-purple-600 hover:bg-purple-700">Learn More About Our Mission</Button>
          </div>
        </div>
      </div>
    </section>
  )
}

