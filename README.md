# reVISit study – Interactive, Web-Based User Studies.  

Create your own interactive, web-based data visualization user studies by cloning/forking and editing configuration files and adding stimuli in the `public` folder. 

reVISit introduces reVISit.spec a DSL for specifying study setups (consent forms, training, trials, etc) for interactive web based studies. You describe your experimental setup in reVISit.spec, add your stimuli as images, forms, html pages, or React components, build and deploy – and you're ready to run your study. For tutorials and documentation, see the [reVISit website](https://revisit.dev). 

## Build Instructions

To run this demo experiment locally, you will need to install node on your computer. 

* Clone `https://github.com/revisit-studies/study`
* Run `yarn install`. If you don't have yarn installed, run `npm i -g yarn`. 
* To run locally, run `yarn serve`.
* Go to [http://localhost:8080](http://localhost:8080) to view it in your browser. The page will reload when you make changes. 

## Release Instructions

Releasing reVISit.dev happens automatically when a PR is merged into the `main` branch. The name of the pull request should be the title of the release, e.g. `v1.0.0`. Releasing creates a tag with the same name as the PR, but the official GitGub release should be created manually. The `main` branch is protected and requires two reviews before merging.

The workflow for release looks as follows:
Develop features on feature branch
| PRs
Dev branch
| PR (1 per release)
Main branch
| Run release workflow on merge
References are updated and commit is tagged

## Assignment Details

Link to the study: https://zrioux10.github.io/zach-rioux-a3/?tab=Others 

Description of our study:
<img width="706" alt="Screenshot 2025-03-06 at 11 59 24 AM" src="https://github.com/user-attachments/assets/98448734-5802-4891-9210-106c096894f4" />

Our study consisted of 12 questions for participants to answer. The idea of this study was to create dots like in a heatmat where two are marked. The objective is to estimate the percentage the lighter dot is relative to the darker dot. In the screenshot above from our tutorial, we show participants the box they will input their value into and three examples with the correct answers shown. At the end of the study we did ask participants three questions to guage if there was any difficulties with the wording or image actually showing. A few individuals reported difficulties understanding the wording of the study and others wanted to see examples of benchmarks for the percentages. Overall the results were positive.

Design Achievements:
- Use and modification of reVISit (we thought this would give the best results)
- Help button brought the participant back to the tutorial
- Closing study questions for further iterations to improve the study if it was done again

Technical Achievements:
- Heatmap coloring for questions
- Color on results graph is mapped to the question it came from
