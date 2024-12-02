import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { BookOpen, Brain, BarChart2, Calendar, CheckCircle } from "lucide-react"
import { GraduationCap } from "lucide-react";

const features = [
  {
    title: "Smart Summarization",
    description: "Condense lengthy notes and textbooks into concise, easy-to-understand summaries.",
    icon: BookOpen,
  },
  {
    title: "Intelligent Question Generation",
    description: "Create tailored multiple-choice and free-response questions to test your knowledge.",
    icon: Brain,
  },
  {
    title: "Performance Analytics",
    description: "Track your progress and identify areas for improvement with detailed insights.",
    icon: BarChart2,
  },
  {
    title: "Adaptive Study Schedules",
    description: "Optimize your study time with AI-generated schedules based on your learning patterns.",
    icon: Calendar,
  },
  {
    title: "Automated Grading",
    description: "Get instant feedback on your practice sessions with AI-powered grading.",
    icon: CheckCircle,
  },
  {
    title: "Free Response Evaluation",
    description: "Receive constructive feedback on your essay-style answers to improve your writing skills.",
    icon: GraduationCap,
  },
]

export function Features() {
  return (
    <section className="py-24 bg-background">
      <div className="container mx-auto px-6 lg:px-12">
        <h2 className="text-5xl font-extrabold text-center mb-16 bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-pink-600">
          Supercharge Your Learning
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-12">
          {features.map((feature, index) => (
            <Card
              key={index}
              className="p-6 bg-background/50 backdrop-blur-sm border-purple-500/20 hover:border-purple-500/40 transition-all duration-300 rounded-lg shadow-lg hover:shadow-xl"
            >
              <CardHeader className="flex flex-col items-center">
                <feature.icon className="h-12 w-12 mb-4 text-purple-500" />
                <CardTitle className="text-2xl font-semibold text-center">
                  {feature.title}
                </CardTitle>
              </CardHeader>
              <CardContent className="text-center">
                <CardDescription className="text-lg text-muted-foreground">
                  {feature.description}
                </CardDescription>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>
    </section>
  );
}