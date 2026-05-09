# Design

_This follows Google's DESIGN.md alpha shape: optional YAML frontmatter for machine-readable design tokens, then canonical `##` sections in order. Remove all italic scaffolding from the final doc._

_When real tokens are settled or directly observed, add YAML frontmatter above this heading with `version: alpha`, `name`, optional `description`, and relevant token groups: `colors`, `typography`, `rounded`, `spacing`, and `components`. Use valid hex colors, px/em/rem dimensions, unitless line heights where appropriate, and `{path.to.token}` references for component tokens. Omit token groups or the entire frontmatter rather than inventing values._

## Overview

_A holistic product or brand style description: audience, personality, density, mood, emotional response, and design principles that guide choices when no token or component rule exists._

## Colors

_Semantic palettes and exact color roles. Include `primary` when colors are known. Name colors by role and optional descriptive name, include hex values when settled, and say where each color should and should not appear._

## Typography

_Type families, levels, hierarchy, readability expectations, weights, line heights, letter spacing, and where each level appears. Use exact fonts and token values only when chosen or observed._

## Layout

_Also known as "Layout & Spacing" in the spec. Grid strategy, max widths, breakpoint posture, spacing scale, density, page rhythm, navigation shape, and responsive behavior._

## Elevation & Depth

_How hierarchy is conveyed: shadows, borders, tonal layers, glass or blur, overlays, focus rings, and layering rules. If the design is flat, say how separation works without shadows._

## Shapes

_Radius scale, geometry, icon style, stroke weight, container shapes, control shapes, and when to break the default shape language._

## Components

_Reusable visual primitives and domain-signature components: buttons, inputs, navigation, cards or lists, chips or tags, tooltips, checkboxes or radios, modals, tables, charts, or other project-standard pieces. Include variants, states, sizing, padding, token references, and accessibility-relevant styling._

## Do's and Don'ts

_Short, forceful guardrails agents can apply directly. Include anti-references and recurring mistakes that would make the UI drift._
