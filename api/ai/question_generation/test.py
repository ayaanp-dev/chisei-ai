from question_generator.questiongenerator import QuestionGenerator
import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
assert device == torch.device('cuda'), "Not using CUDA. Set: Runtime > Change runtime type > Hardware Accelerator: GPU"

qg = QuestionGenerator()

text = '''
Unit Four
The Civil War and Reconstruction
1848 - 1877

DIRECTIONS:	This is your study resource to use as we progress through our unit.  It lists objectives, concepts, terms, and an outline of items that may appear on the unit exam or the AP Exam.

READING ASSIGNMENTS:	Pageant, Chapters 18—22
			Taking Sides #14 
			Taking Sides #17
Various Historical Documents (as assigned.)

READING OBJECTIVES AND REVIEW QUESTIONS:

As you familiarize yourself with these terms, it is important to not only DEFINE or IDENTIFY the term, but also to know the term’s importance.  Why is it important?  How does it relate to the period we are studying?  What relationship does a term have to another term on the list?  IF YOU MERELY IDENTIFY OR DEFINE THE TERM WITHOUT KNOWING ITS IMPORTANCE YOU WILL FIND IT DIFFICULT TO SUCCEED ON TESTS AND QUIZZES. 

Reading objectives are short answer questions that will help you tie together the important information from the chapter.  Answers should be thorough and provide specific evidence.

Chapter 18

Key Vocabulary



“Fire eaters”
“Higher Law” William Seward
“Popular Sovereignty”
“Seventh of March” Speech
California Gold Rush
Clayton-Bulwer Treaty, 1850
Commodore Perry
Compromise of 1850
Election of 1848
Election of 1852
Franklin Pierce
Free Soil Party
Fugitive Slave Law, 1850
Gadsden Purchase
Harriet Tubman
Kansas-Nebraska Act, 1854
Know Nothing Party
Lewis Cass
Ostend Manifesto
Stephen Douglas
Underground Railroad
William Walker
Young America Movement
Zachary Taylor



Reading Objectives:

Explain how the issue of slavery in the territories acquired from Mexico disrupted American politics from 1848—1850.
Point out the major terms of the Compromise of 1850 and indicate how this agreement attempted to deal with the issue of slavery.
Indicate how the Whig party disintegrated and disappeared because of its divisions over slavery.
Describe how a free-soil movement arose that portrayed the expansion of slavery as incompatible with free labor
Describe how the Pierce administration engaged in various prosouthern overseas and expansionist ventures.
Describe Douglas’s Kansas-Nebraska Act and explain why it stirred the sectional controversy to new heights.
Describe the causes and effects of the collapse of the 2nd Party System.

Chapter 19

Key Vocabulary


“Bleeding Kansas”
“self determination”
1860 Election
Abraham Lincoln
American Party
Charles Sumner
Constitutional Union Party
Crittenden Compromise
Dred Scott v. Sandford (1857)
Election of 1856
Freeport Doctrine
Harpers Ferry
Harriet Beecher Stowe
Hinton Rowan Helper
Jefferson Davis
John Brown
James Buchanan
Lecompton Constitution
Lincoln-Douglas Debates
New England Immigrant Aid Society
Panic of 1857
Pottawatomie Massacre
Preston Brooks
Republican Party
South Carolina Secession
The Impending Crisis of the South
Uncle Tom’s Cabin


Reading Objectives:

Relate the sequence of major crises that led from the Kansas-Nebraska Act to secession.
Explain how and why “bleeding Kansas” became a dress rehearsal for the Civil War.
Describe how African American and white abolitionists, although a minority in the North, mounted a highly visible campaign against slavery, presenting moral arguments against the institution, assisting slaves’ escapes, and sometimes expressing a willingness to use violence to achieve their goals
Trace the growing power of the Republican Party in the 1850s and the increasing divisions and helplessness of the Democrats.
Explain how the Dred Scott decision and Brown’s Harpers Ferry raid deepened sectional antagonism.
Trace the rise of Lincoln as the leading exponent of the Republican doctrine of no expansion of slavery.
Analyze the complex election of 1860 in relation to the sectional crisis.
Describe the movement toward secession, the formation of the Confederacy, and the failure of the last compromise effort.




Chapter 20

Key Vocabulary


Alabama
Conscription Act
Draft Riots
Ex parte Merriman (1861)
Ex parte Milligan (1866)
Fort Sumter
Greenbacks
Habeas Corpus
Homestead Act, 1862
Jefferson Davis
Morrill Land Grant Act, 1862
Morrill Tariff Act
Napoleon III
National Banking Act, 1863
Pacific Railway Act, 1862
Peace Democrats
Trent Affair
Ulysses S. Grant



Reading Objectives:

Explain how the firing on Fort Sumter and Lincoln’s call for troops galvanized both sides for war.
Indicate the strengths and weaknesses of both sides as they went to war.
Describe the diplomatic struggle for the sympathies of the European powers.
Describe the curtailment of civil liberties that occurred during the Civil War.
How westward migration was boosted during and after the Civil War by the passage of new legislation promoting Western transportation and economic development.
Analyze the economic and social consequences of the war for both sides.

Chapter 21

Key Vocabulary


“March to the Sea”
13th Amendment
Abraham Lincoln
Andrew Johnson
Appomattox Court House
Assassination of Lincoln
Battle of Antietam
Bull Run
Copperheads
Election of 1864
Emancipation Proclamation
George McClellan
Gettysburg Address
John Wilkes Booth
Massachusetts 54th
Robert E. Lee
Thomas “Stonewall” Jackson
Ulysses S. Grant
Union Party
William T. Sherman



Reading Objectives

Describe the purpose of the Civil War and how that purpose transformed throughout the course of war.
Describe the failure of the North to gain its expected early victory in 1861.
Summarize the Gettysburg address and describe its significance.
Describe how the Union ultimately succeeded due to improvements in leadership and strategy, key victories, greater resources, and the wartime destruction of the South’s infrastructure
Describe the role that African Americans played during the war.
Describe the political struggle between Lincoln’s “Union party” and the antiwar Copperheads.
Describe the end of the war and list its final consequences.

Chapter 22

Key Vocabulary


“40 acres and a mule”
“Exodusters”
“Lost Cause”
“Seward’s Folly”
“Swing around the circle”
10% Plan
13th Amendment
14th Amendment
15th Amendment
Andrew Johnson
Black Codes
Carpetbaggers
Charles Sumner
Civil Rights Act, 1866
Conservative, Moderate, 
Radical Republicans
Crop lien
Ex parte Milligan (1866)
Force Acts, 1870-71
Freedmen’s Bureau
Johnson Impeachment
Ku Klux Klan
Military Reconstruction Act, 1867
Pocket Veto
Scalawags
South “Redeemed”
Tenure of Office Act, 1867
Thaddeus Stevens
Wade Davis Bill



Reading Objectives

Define the major problems facing the South and the nation after the Civil War.
Describe the responses of both whites and African-Americans to the end of slavery.
Analyze the differences between the presidential and congressional approaches to Reconstruction.
Describe how the women’s rights movement was both emboldened and divided over the Fourteenth and Fifteenth Amendments to the Constitution
Explain how the blunders of President Johnson and the white South opened the door to more radical congressional Reconstruction policies.
Describe the actual effects of congressional Reconstruction in the South.
Indicate how militant white opposition gradually undermined the Republican attempt to empower Southern blacks.
Explain why the radical Republicans impeached Johnson but failed to convict him.

Unit Review Questions:

Describe how U.S. interest in expanding trade led to economic, diplomatic, and cultural initiatives to create more ties with Asia.
What were the long- and short-term causes of the Civil War?
Using evidence from the unit, explain how interpretations of the Constitution and debates over rights, liberties, and definitions of citizenship have affected American values, politics, and society.
Using evidence from the unit, explain how ideas about democracy, freedom, and individualism found expression in the development of cultural values, political institutions, and American identity.
Explain how different beliefs about the federal government’s role in U.S. social and economic life have affected political debates and policies.
Identify key turning points in the Civil War. Which is the most significant? Why?
Describe how Reconstruction and the Civil War ended slavery, altered power relationships between the states and the federal government, and led to debates over new definitions of citizenship.
Explain continuities and changes in race relations in the South from 1865-1877.
Explain the legacy of Reconstruction, and assess its successes and failures.

Presidency Charts

Zachary Taylor/Millard Fillmore
Franklin Pierce
James Buchanan
Abraham Lincoln
Andrew Johnson
'''

q_list = qg.generate(text, num_questions=10)
for q in q_list:
    print(q)